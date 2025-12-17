pipeline {
  agent any

  environment {
    IMAGE_NAME = 'awaismalak/log-aggregator'
    IMAGE_TAG = 'latest'
  }

  stages {
    stage('Clone Repository') {
      steps {
        echo '📥 Cloning project from GitHub...'
        git url: 'https://github.com/Malikawais108/log-aggregator.git', branch: 'main'
      }
    }

    stage('Build Docker Image') {
      steps {
        echo '🔧 Building Docker image from root-level Dockerfile...'
        sh '''
          docker build -t $IMAGE_NAME:$IMAGE_TAG .
        '''
      }
    }
    stage('Run Tests') {
      steps {
        echo '🧪 Running unit/integration tests...'
        sh '''
           docker run --rm $IMAGE_NAME:$IMAGE_TAG pytest --maxfail=1 --disable-warnings -q
        '''
  }
}


    stage('Run Exporter') {
      steps {
        echo '🧪 Running container to validate exporter...'
        sh '''
          docker run --rm $IMAGE_NAME:$IMAGE_TAG python main.py &
          sleep 5
        '''
      }
    }

    stage('Push to Docker Hub') {
      steps {
        echo '🚀 Pushing image to Docker Hub...'
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
            docker push $IMAGE_NAME:$IMAGE_TAG
          '''
        }
      }
    }

    stage('Cleanup Workspace') {
      steps {
        echo '🧹 Cleaning up workspace...'
        cleanWs()
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
