pipeline {
  agent any
  stages {
    stage('-- Git clone from WoG repository --') {
      steps {
        git branch: 'main', url: 'https://github.com/wittydavid/WorldOfGames.git'
      }
    }
    stage('-- Create dummy scores.txt file --') {
      steps {
        sh 'echo 55 > scores.txt'
        sh 'ls -ltr'
      }
    }
    stage('-- Install docker compose in container --') {
      steps {
        sh 'sudo curl -L --fail https://github.com/docker/compose/releases/download/1.29.2/run.sh -o /usr/local/bin/docker-compose'
        sh 'sudo chmod +x /usr/local/bin/docker-compose'
      }
    }
    stage('-- Start and stop the flask app --') {
      steps {
        sh 'docker-compose up -d'
        sh 'docker ps -a'
        sh 'docker-compose down'
      }
    }
    stage('-- Run e2e tests : by default sh will fail the pipe if exit code != 0 --') {
      steps {
        sh 'python tests/e2e.py'
      }
    }
    stage('-- Push the images to dockerhub --') {
      steps {
        sh 'python tests/e2e.py'
      }
    }
  }
}

// This Jenkins job will
// 1. clone the world of games repo
// 2. create a dummy scores.txt file
// 3. will run the docker-compose file
// 4. run e2e tests
// 5. if test pass push to dockerhub images, otherwise terminate



