pipeline {
    agent any

    environment {
        PYTHON_SCRIPT = '''
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

            SELENIUM_GRID_URL = "http://<your-selenium-grid-hub-url>:4444/wd/hub"
            capabilities = DesiredCapabilities.CHROME.copy()
            driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities=capabilities)

            driver.get("https://www.python.org")
            print(driver.title)
            search_bar = driver.find_element_by_name("q")
            search_bar.clear()
            search_bar.send_keys("getting started with python")
            search_bar.send_keys(Keys.RETURN)
            print(driver.current_url)
            driver.close()
        '''
    }

    stages {
        stage('Setup Environment') {
            steps {
                // Install Selenium and other dependencies
                sh 'pip install selenium'
            }
        }

        stage('Run Selenium Script') {
            steps {
                script {
                    writeFile file: 'selenium_test.py', text: env.PYTHON_SCRIPT
                    sh 'python selenium_test.py'
                }
            }
        }
    }

    post {
        always {
            // Clean up
            deleteDir()
        }
    }
}
