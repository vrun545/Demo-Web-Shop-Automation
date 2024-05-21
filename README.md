
# Automated Testing Framework for DemoWebShop

This repository contains a pytest framework for automated testing of the DemoWebShop website. The framework includes the following features:

## Features

- **Test Cases**: Automates various test cases for the DemoWebShop website, covering functionalities such as account creation, login, profile management, and search functionality.
  
- **External Test Data**: Test data such as usernames, passwords, and addresses are passed using a `config.ini` file for easy management and customization.

- **Modular Architecture**: Utilizes a modular architecture with Python package structure, promoting organization and maintainability.

- **Global Configuration**: Main global configuration such as browser and URL is kept in a separate file for easy customization.

- **Command Line Execution**: Tests can be executed from the command prompt, allowing for easy integration into continuous integration pipelines.

- **Headless and Non-Headless Mode**: Tests are executable on both headless and non-headless modes for Chrome and Firefox browsers.

- **Pytest Features**: Utilizes pytest features for organized test cases, parameterization, fixtures, and now logging functionality.

- **Page Object Model (POM)**: Implements the Page Object Model for improved code readability and maintainability.

- **HTML Report**: Generates an HTML test report after test execution for better visualization of test results.

- **Tagging**: Tags are implemented for each test case, allowing for selective test execution.

- **Logging**: Logging functionality has been added to provide detailed information during test execution for better debugging and analysis.

## Usage

Certainly! Here's a paragraph you can add to your README file:

```markdown
## Running Tests on Specific Browser and Headless Mode

You can run the test cases on specific browsers and in headless mode by specifying options when running pytest. Use the following commands to execute the tests:

- **Run tests on Chrome browser**:
```bash
pytest -v -k "chrome"
```

- **Run tests on Firefox browser**:
```bash
pytest -v -k "firefox"
```

- **Run tests in headless mode**:
```bash
pytest -v -k "headless"
```

You can combine these options as needed. For example, to run tests on Chrome browser in headless mode:
```bash
pytest -v -k "test_LoginFeature.py and headless" -s
```

Feel free to adjust the options according to your requirements and browser configurations.
```

Feel free to customize this paragraph according to your specific test setup and requirements!

- Tests can be run selectively using pytest options such as `-k` for specific test names or `-m` for tags.
- HTML test report can be generated using the `--html` flag followed by the desired report file name.

## Contributing

Contributions are welcome! Please feel free to submit a pull request for any improvements, bug fixes, or additional features.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.
``` 
