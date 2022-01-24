# Sigma Flow-Shop Scheduling

![Cover](https://i.imgur.com/KHWTupe.jpg)

## Description

Sigma is a tool that allows to calculate the Makespan, the Tardiness and the Sequence of a flow-shop optimization problem of `n` jobs and `m` machines, taking in consideration the setup time and the due dates.

## Sigma v0.2 Features

### Set the parameters

![Main](https://i.imgur.com/MAhNlmR.png)

- It can optimize a flow-shop problem with `n` jobs and `m` machines.
- It allows you to choose the parameter to optimize.
  - Makespan
  - Tardiness
  - Makespan with setup time

### Import Data

![Import](https://i.imgur.com/QaYSDXR.png)

- Import data from Excel Spreadsheets
- Insert data manually

### Visualize Data

![Plots](https://i.imgur.com/oNZQhus.png)

- Clean and readable charts

## How to Install and Run `Setup.exe`

<p align="center">
<img src="https://i.imgur.com/qxTf3Jx.png" title="source: imgur.com" />
</p>

You can download the `setup.exe` file from the following links:

<p align="center">
<img src="https://i.imgur.com/MU39G42.png" title="source: imgur.com" />
</p>

- MediaFire: [Sigma v0.2](https://www.mediafire.com/file/n1lm9f2airkjzob/setupSigma_v0.2.exe/file)
- Google Drive: [Sigma v0.2](https://drive.google.com/file/d/1DGtkNNhTyQXGSvePanuuEBrqBD7fqKMS/view)

And to install you can follow the installation guide:
![Installation](https://i.imgur.com/k7WQb5h.png)

Enjoy!!

## How to Install and Run `Python`

You need to install python v3 or a higher version to run this project on your machine.

Clone the repository and `cd` to the project folder, open you favorite command line and type the following commands:

- Create a virtual environment:

```bash
python -m venv venv
```

- Activate the virtual environment:

```bash
./venv/Scripts/activate
```

- Install dependencies:

```bash
pip install -r ./requirements.txt
```

- Run the project:

```bash
python src/sigma.py
```

## How to Use Sigma v0.2

It is simple to use, you only have to take in consideration the supported Excel spreadsheets format `.xlsx` to import it successfully. Other than that it is simple to use.

> The first cell from the imported file is `B2`, because it counts the headers.

## Credits

This project was made possible with the effort of three students:

- [Aala Eddine Bousskoul](https://github.com/aalaebl)
- [Ayoub Taoufik](https://github.com/taoufikayoub)
- [Yassine Amedouz]()

## License

[Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
