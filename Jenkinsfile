// pipeline {
//     agent any
//     stages {
//         stage('Pull Lastest Image') {
//             steps {
//                 bat "docker pull pthpoa/selenium-docker"
//             }
//         }
//         stage('Start grid') {
//             steps {
//                 bat "docker-compose up -d hub chrome firefox"
//             }
//         }
//         stage('Run Test') {
//             steps {
//                 bat "docker-compose up search-module"
//             }
//         }
//     }
//     post{ 
//         always{
//             archiveArtifacts artifacts: 'output/**'
//             bat "docker-compose down"
//         }
//     }
// }
pipeline{
	agent any
	stages{
		stage("Pull Latest Image"){
			steps{
				sh "docker pull pthpoa/selenium-docker"
			}
		}
		stage("Start Grid"){
			steps{
				sh "docker-compose up -d hub chrome firefox"
			}
		}
		stage("Run Test"){
			steps{
				sh "docker-compose up search-module"
			}
		}
	}
	post{
		always{
			archiveArtifacts artifacts: 'output/**'
			sh "docker-compose down"
			sh "sudo rm -rf output/"
		}
	}
}