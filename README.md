# 🚀 Sublime Streamlit

[![Downloads](https://img.shields.io/packagecontrol/dt/Streamlit)](https://packagecontrol.io/packages/Streamlit)
[![Tag](https://img.shields.io/github/v/tag/futureprogrammer360/Sublime-Streamlit?sort=semver)](https://github.com/futureprogrammer360/Sublime-Streamlit/tags)
[![Repo size](https://img.shields.io/github/repo-size/futureprogrammer360/Sublime-Streamlit)](https://github.com/futureprogrammer360/Sublime-Streamlit)
[![License](https://img.shields.io/github/license/futureprogrammer360/Sublime-Streamlit?style=flat-square)](https://github.com/futureprogrammer360/Sublime-Streamlit/blob/master/LICENSE)

[Sublime Streamlit](https://github.com/futureprogrammer360/Sublime-Streamlit) is a [Sublime Text](https://www.sublimetext.com/) package for Python's [Streamlit](https://streamlit.io/) library, providing completion, build system, and documentation.

## 💻 Installation

The easiest way to install Sublime Streamlit is through [Package Control](https://packagecontrol.io/packages/Streamlit). After it is enabled inside Sublime Text, open the command palette and find **Package Control: Install Package** and press `ENTER`. Then, find **Streamlit** in the list. Press `ENTER` again, and this package will be installed!

## 📈 Usage

### Completion

Sublime Streamlit provides completion for all Streamlit commands. The full list of completions can be found in the [`streamlit.sublime-completions`](https://github.com/futureprogrammer360/Sublime-Streamlit/blob/master/streamlit.sublime-completions) file.

### Build

Sublime Streamlit adds a new build system, [`Streamlit`](https://github.com/futureprogrammer360/Sublime-Streamlit/blob/master/Streamlit.sublime-build), which uses `streamlit run` to run a Streamlit program.

### Documentation

Sublime Streamlit has two commands for exploring Streamlit docs.

In a program, select a Streamlit command (example: `st.write`) and run the `Streamlit: Doc` command in the command palette to open the command's Streamlit documentation page in the browser.

To search for the documentation of a Streamlit command, run the `Streamlit: Search Doc` command in the command palette. Select the desired command to open its documentation page in the browser.
