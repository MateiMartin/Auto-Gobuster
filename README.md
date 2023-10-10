# Auto-Gobuster

## Motivation

I wanted to execute a single command that would identify all possible sub-URLs or sub-links from a website and to use it as part of a normal web pentest.

## Description
This is a python script that runs gobuster again for every good url found (200,301...)

## Usage

```
python3 autogobuster -h 
```
Example:

```
autogobuster -u http://0.0.0.0/ -w ~/wordlists/urls/common.txt
```

## Requirements
You need to have gobuster added to the gloabl path. </br>
If you dont't have gobuster you can get it from here https://github.com/OJ/gobuster

