# BlueprintLX

## Project Overview
This project provides an automation framework for setting up a new Linux environment. It's designed to be flexible, allowing users to easily add or remove setup components via plugins. The framework currently supports Ubuntu but can be adapted for other Linux distributions.

## Features
- **Automated Basic Setup**: Automatically updates and upgrades the system using apt.
- **Extensible Plugin System**: Easily extend the framework with custom plugins for additional tools and configurations.
- **Real-time Output**: View the output of each installation process in real-time.

## Getting Started

### Prerequisites
- A Linux system (preferably Ubuntu)
- Python 3
- Git (for some plugins)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/leopck/BlueprintLX.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd BlueprintLX
   ```

### Usage
- Run the main script to execute the base setup and any enabled plugins:
  ```bash
  python3 main.py
  ```

## Plugins
### Existing Plugins
- **Vim Setup**: Installs Vim and configures it.
- **Zsh with Powerlevel10k**: Sets up Zsh with the Powerlevel10k theme and necessary fonts.

### Writing New Plugins
1. Create a new Python script in the `plugins` directory.
2. Define a class with the same name as the script (capitalized).
3. Implement a static `run` method with the installation commands.
4. The plugin will be automatically detected and run by the main script.

## Contributing
Contributions to this project are welcome! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
