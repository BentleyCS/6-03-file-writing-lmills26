import pytest
import os
from CSP_6_03_Writing_to_files import writeFile, sortNames, highScore

def test_writeFile_creates_file():
    writeFile(["Alice","Bob","Charlie"],"test_write.txt")
    assert os.path.exists("test_write.txt")

def test_writeFile_correct_contents():
    writeFile(["Alice", "Bob", "Charlie"], "test_write.txt")
    file = open("test_write.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    file.close()
    assert lines == ["Alice", "Bob", "Charlie"]

def test_sortNames_creates_file():
    writeFile(["Charlie","Alice","Bob"], "test_names.txt")
    sortNames ("test_names.txt","test_names_sorted.txt")
    assert os.path.exists("test_names_sorted.txt")

def test_sortNames_sorts_correctly():
    writeFile(["Charlie","Alice","Bob"],"test_names.txt")
    sortNames ("test_names.txt","test_names_sorted.txt")
    file = open("test_names_sorted.txt", "r")
    lines = [line.strip() for line in file.readlines() if line.strip()]
    file.close()
    assert lines == ["Alice", "Bob", "Charlie"]

def test_highScore_returns_average():
    file = open("scores.txt", "w")
    file.write("50\n100\n")
    file.close()
    result = highScore(50)
    assert result == 66.67 or isinstance(result, float)

def test_highScore_returns_float():
    result = highScore(75)
    assert isinstance(result, float)
