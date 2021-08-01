pipeline {
  agent any
  stages {
    stage('-- Git clone from WoG repository --') {
      steps {
        git 'https://github.com/wittydavid/WorldOfGames.git'
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