pipeline{
    agent{
        node{
            label 'agent-video'
        }
    }
    triggers{
        pollSCM '*/10 * * * *'
    }
    stages{
        stage('Build'){
            steps {
                echo "Build stage ..."
                sh '''
                python3 -m venv .venv
                .venv/bin/python --version
                . ./venv/bin/activate
                python -m pip install -r requirements.txt
                deactivate
                '''
            }
        }
        stage('Test'){
            steps {
                echo "Test stage..."
                sh '''
                . ./venv/bin/activate
                python ./pis-etap3/mysite/tests/test_example.py
                '''
            }
        }
        stage('Deliver'){
            steps {
                echo "Deliver stage..."
            }
        }
    }
}