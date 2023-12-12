import importlib


"""
    This factory is responsible for creating the application instance
    @:param app(STRING): The name of the application
    @:param args(LIST): The arguments of the application
    @:param output(DEQUE): The output of the application
    @:return instance(APPLICATION): The instance of the specific application
    @:raise ImportError and ValueError: If the application is not supported
"""


def application_factory(app, args, output):
    try:
        # Debugging: Print the apps, arguments and outputs
        # print(app)
        # print(args)
        # print(output)

        # import the module and get the class
        app_name = app.capitalize()
        app_module = importlib.import_module(f'applications.{app_name}')

        # Debugging: Print the imported module and class
        # print("Imported module:", app_module)
        app_class = getattr(app_module, app_name)
        # print("Found class:", app_class)

        instance = app_class(args, output)
        # Debugging: Print the instance
        # print("Created instance:", instance)

        return instance

    except (ImportError, AttributeError):
        # print(f"Error occurred: {e}")
        raise ValueError(f"Unsupported application {app}")
