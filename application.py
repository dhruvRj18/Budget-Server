from budget_server import application
from budget_server.api.route import init_api_blueprint

application.register_blueprint(init_api_blueprint())

if __name__ == '__main__':
    application.run(host='0.0.0.0',debug=True)

