from script import *

def test_sample():
    data  = """
        {
            "FolderA": {
                "_files": [ "file1", "file2" ] ,
                "SubfolderC": {
                    "_files": [ "file1" ]
                } ,
                "SubfolderB": {
                    "_files" : [ "file1" ]
                }
            }
        }
    """
    assert(fileSearch("file1", data) ==
           ["/FolderA/file1",
            "/FolderA/SubfolderB/file1",
            "/FolderA/SubfolderC/file1",])

def test_readme():
    assert(fileSearch("file", '{"_files":["file", "fileA"], "dirA":{}}') == ['/file'])

if __name__ == "__main__":
    test_sample()
    test_readme()
