import json

"""
Find all path to the files in the `obj` with the name `filename`.
Return list of path where path is a list of string of directory name and file name.
ex. [ ['path', 'to', 'file1'], ['anotherpath', 'file1'] ]

The obj should be formatted like this:
{
     "_files": [ "fileA", "fileB", ...]
     , "directoryA": <a's Obj>
     , "directoryB": <b's Obj>
     , ...
}
"""
def findFiles(obj, filename, prefix = []):
    result = []
    for k, v in obj.items():
        if k == "_files":
            if filename in v:
                result.append(prefix + [filename])
        else:
            # Assume the k doesn't start with '_' as stated
            result += findFiles(v, filename, prefix + [k])
    return result

"""
Search for all files in filesObj json string and 
return list of path string ordered by depth-level and its lexicographical order
"""
def fileSearch(fileToSearch, filesObj):
    jsonObj = json.loads(filesObj)
    result = findFiles(jsonObj, fileToSearch)
    topath = lambda x : '/' + '/'.join(x)
    result = [topath(p) for p in sorted(result, key=lambda x:(len(x), topath(x)))]
    return result
