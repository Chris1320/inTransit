# inTransit

inTransit is a School Canteen Automated Reporting System.

![Frontend Tests](https://github.com/Chris1320/inTransit/actions/workflows/frontend.yml/badge.svg)
![Super Linter](https://github.com/Chris1320/inTransit/actions/workflows/super-linter.yml/badge.svg)

## Development

**Stack**:

- [Next.js](https://nextjs.org/)
  - [Chakra UI](https://www.chakra-ui.com/)
- [Firebase](https://firebase.google.com/)
  - [Authentication](https://firebase.google.com/docs/auth)
  - [Firestore](https://firebase.google.com/docs/firestore)
  - [Functions](https://firebase.google.com/docs/functions)
    - [Python](https://www.python.org/)

**Project Management Software**:

- Node.js: [nvm](https://github.com/nvm-sh/nvm)/[nvm for Windows](https://github.com/coreybutler/nvm-windows)
- Python: [uv](https://astral.sh/uv) & [pip](https://pip.pypa.io/en/stable/)

### Development Environment Installation & Setup

Follow the steps below to set up your development environment on Windows or Linux
systems. It assumes that you have a terminal open in the project's root directory.

#### 1. Install Package Managers and Related Software

The central server is hosted on Google [Firebase](https://firebase.google.com/).
[nvm-windows](https://github.com/coreybutler/nvm-windows) is recommended to be
used to install and manage Node. [Python](https://python.org/) is used to test
Firebase functions.

> [!CAUTION]
> Make sure to remove previous installations of Python and NodeJS before
> proceeding. If you are certain that there are no traces left of the previous
> installation (i.e., leftover configuration files), you can perform the
> following commands:

```powershell
git clean -dfx
git restore .

winget install astral-sh.uv
uv python install 3.13.1
winget install CoreyButler.NVMforWindows
nvm install 23.6.1
nvm use 23.6.1
npm install -g firebase-tools

# Confirm successful installation of packages
python --version  # Python 3.13.1
node --version    # v23.6.1
npm --version     # 10.9.2
```

> [!NOTE]
> The commands below assumes that your Linux distribution is using `apt` as your
> package manager.

```bash
git clean -dfx
git restore .

sudo apt update && sudo apt install curl
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12.8
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
nvm install 23.6.1
nvm use 23.6.1
npm install -g firebase-tools

# Confirm successful installation of packages
python --version  # Python 3.13.1
node --version    # v23.6.1
npm --version     # 10.9.2
```

You should add nvm's init script to your `.profile` to make sure that the node
path is always loaded.

#### 2. Visual Studio Code

Any IDE would work, but using [Visual Studio Code](https://code.visualstudio.com/)
is recommended. It is also recommended to install the following extensions:

- Black Formatter
- ES7+ React/Redux/React-Native snippets
- ESLint
- Git
- HTML CSS Support
- IntelliCode
- IntellCode API Usage Examples
- isort
  - Add `--profile black` to isort args in preferences.
- JavaScript (ES6) code snippets
- Path Intellisense
- Prettier - Code formatter
  - Set _print width_ to `120` in preferences.
  - Set _tab width_ to `4` in preferences.
- Pylance
- Pylint
  - Set _import strategy_ to `fromEnvironment` in preferences.
- Python
  - Enable _Pytest Enabled_ in preferences.
- Python Debugger
- Tailwind CSS IntelliSense

#### 3. Replicate Environment Setup

To make sure that every collaborator has the same environment, execute the
following commands:

> [!CAUTION]
> Some of the commands below are **destructive**. Make sure to commit your
> changes or they will be gone!

In the project root, run the following:

```powershell
python -m venv .\functions\venv
.\functions\venv\Scripts\Activate.ps1
pip install -r .\functions\requirements.txt

cd .\intransit
npm install
```

#### 4. Test The Environment

```powershell
firebase emulators:start
```

```powershell
node run dev
```

Make sure all services are accessible locally.
