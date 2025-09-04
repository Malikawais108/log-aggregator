pipeline {
  agent any

  environment {
    IMAGE_NAME = 'awaismalak/log-aggregator'
    IMAGE_TAG = 'latest'
    HELM_RELEASE = 'log-aggregator'
    HELM_CHART_PATH = './helm'
  }

  stages {
    stage('SonarQube Analysis') {
      steps {
        echo '🔍 Running SonarQube code quality scan...'
        withSonarQubeEnv('MySonarQubeServer') {
          withCredentials([string(credentialsId: 'TOKEN_ID', variable: 'SONAR_TOKEN')]) {
            sh """
              sonar-scanner \
                -Dsonar.projectKey=log-aggregator \
                -Dsonar.sources=parser \
                -Dsonar.language=py \
                -Dsonar.login=$SONAR_TOKEN
            """
          }
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        echo '🔧 Building Docker image...'
        sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ./parser"
      }
    }

    stage('Push to Docker Hub') {
      steps {
        echo '🚀 Pushing image to Docker Hub...'
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
          sh "docker push $IMAGE_NAME:$IMAGE_TAG"
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        echo '📦 Deploying to Kubernetes with Helm...'
        sh "helm upgrade --install $HELM_RELEASE $HELM_CHART_PATH --set image.repository=$IMAGE_NAME --set image.tag=$IMAGE_TAG"
      }
    }
  }

  post {
    success {
      echo '✅ Pipeline completed successfully!'
    }
    failure {
      echo '❌ Pipeline failed. Check logs for details.'
    }
  }
}
