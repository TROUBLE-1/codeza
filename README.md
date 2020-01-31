# Description
This tool will scan all the URL's in the file and will provide Content-Length and Status-Code. 
Result will be saved in different files
This tool will help to select the target when you have 1000 of domains

# Note
I have provided a list of subdomins of \*.ford.com with more then 5000 domins

## Usage
Provide file_name, min_content_length, Folder_name_to_create respectively
Make sure Files contains URL's with http:// or https://

```
python codeza.py alive.txt 500 ford
```
## When to use this ?
1. Get all list of subdomains in a file (eg. all.txt)
2. use httprobe command (eg. cat all.txt | httprobe > alive.txt) --> https://github.com/tomnomnom/httprobe
   Now Use codeza.py to enumerate all urls about its Content-Length and status code 
3. ```python codeza.py alive.txt 500 ford```
