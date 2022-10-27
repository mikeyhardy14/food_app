import configure_new_token
import webApplication

if __name__ == '__main__':
    print('Configuring New Token...')
    token = configure_new_token.get_access_token()
    print('Token Configured!')
    print('Launch Web App')
    webApplication.app.run()


