## Pre-requisites to be installed

### For Ubuntu users

```
sudo apt install astyle cmake gcc ninja-build libssl-dev python3-pytest python3-pytest-xdist unzip xsltproc doxygen graphviz python3-yaml valgrind
```

### For Mac Users

```
brew install cmake ninja openssl@3 wget doxygen graphviz astyle valgrind
pip3 install pytest pytest-xdist pyyaml
```

---

## Installation (Same as the one provided by the official repo for liboqs-python)

Refer the official repo for the installation of libraries : [Liboqs-Python](https://github.com/open-quantum-safe/liboqs-python/tree/main)

### Install and activate a Python virtual environment

Execute in a Terminal/Console/Administrator Command Prompt

```shell
python3 -m venv venv
. venv/bin/activate
python3 -m ensurepip --upgrade
```

On Windows, replace the line

```shell
. venv/bin/activate
```

by

```shell
venv\Scripts\activate.bat
```

### Configure and install the wrapper

Execute in a Terminal/Console/Administrator Command Prompt

```shell
pip install .
```

## Running the project

```
python3 main.py
```

## Limitations and security

liboqs is designed for prototyping and evaluating quantum-resistant
cryptography. Security of proposed quantum-resistant algorithms may rapidly
change as research advances, and may ultimately be completely insecure against
either classical or quantum computers.

We believe that the NIST Post-Quantum Cryptography standardization project is
currently the best avenue to identifying potentially quantum-resistant
algorithms. liboqs does not intend to "pick winners", and we strongly recommend
that applications and protocols rely on the outcomes of the NIST
standardization project when deploying post-quantum cryptography.

We acknowledge that some parties may want to begin deploying post-quantum
cryptography prior to the conclusion of the NIST standardization project. We
strongly recommend that any attempts to do make use of so-called
**hybrid cryptography**, in which post-quantum public-key algorithms are used
alongside traditional public key algorithms (like RSA or elliptic curves) so
that the solution is at least no less secure than existing traditional
cryptography.

Just like liboqs, liboqs-python is provided "as is", without warranty of any
kind. See
[LICENSE](https://github.com/open-quantum-safe/liboqs-python/blob/main/LICENSE)
for the full disclaimer.

---

## License

liboqs-python is licensed under the MIT License; see
[LICENSE](https://github.com/open-quantum-safe/liboqs-python/blob/main/LICENSE)
for details.

---

### Acknowledgments to the contributors of OQS library

Contributors to the liboqs-python wrapper include:

- Ben Davies (University of Waterloo)
- Vlad Gheorghiu ([softwareQ Inc.](https://www.softwareq.ca) and the University
  of Waterloo)
- Christian Paquin (Microsoft Research)
- Douglas Stebila (University of Waterloo)

---