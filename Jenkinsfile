pipeline {
	agent any
	//agent { docker { image 'python:3.7.2' } }
	trigger{
		pollSCM('* * * * *')
		cron('0 0 0 * * *')
	}
 	stages {
 		stage("Compile") {
 			steps {
 				echo "no need to build python code"
 			}
 		}
 		stage("Unit test") {
 			steps {
 				sh "python3 test_code.py"
 			}
 		}
 	}
}
