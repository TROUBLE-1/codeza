# Description
This tool will scan all the URL's in the file and will provide Content-Length and Status-Code. 
Result will be saved in different files
This tool will help to select the target when you have 1000's of domains

  ____   ____   ____   _____  _____      _
 |####| |####| |####  |##### |#####     /#\   
|#      #    # |#   # |#|___    /#     /# #\     
|#      #    # |#   # |####    /#     /#__\#\    
|#____  #____# |# __# |#|__   /#     /#/   \#\         
 |####| |####| |####  |##### /##### /#/     \#\     

# Note
I have provided a list of subdomins of \*.ford.com with more then 5000 domins.

Provide file_name, min_content_length, Folder_name_to_create respectively while using codeza.py

Make sure file contains URL's with http:// or https://

# Usage
1. Get all list of subdomains in a file (eg. all.txt)
2. use httprobe command (eg. cat all.txt | httprobe > alive.txt) --> https://github.com/tomnomnom/httprobe
  Now Use codeza.py to enumerate all urls about its Content-Length and status code 
3. ```python codeza.py alive.txt 500 ford```

```
root@kali:~/recon/tagert# python codeza.py alive.txt 500 ford
root@kali:~/recon/tagert# cd ford/
root@kali:~/recon/tagert/ford# ls
contains_form.txt possible_Dom_XXS.txt potential_result.txt  potential.txt  status with_titles.txt
root@kali:~/recon/tagert/ford# cd status/
root@kali:~/recon/tagert/ford/status# ls
200.txt  301.txt  302.txt  303.txt  400.txt  401.txt  403.txt  404.txt  500.txt  502.txt  503.txt
root@kali:~/recon/tagert/ford/status# cat 200.txt | wc -l
926
root@kali:~/recon/tagert/ford/status# cat 404.txt | wc -l
137
root@kali:~/recon/tagert/ford/status# cat 500.txt | wc -l
17
root@kali:~/recon/tagert/ford/status# cat 303.txt | wc -l
3
root@kali:~/recon/tagert/ford/status# 

```
Twitter- https://twitter.com/trouble1_raunak

Youtube- https://www.youtube.com/channel/UCkJ_sEF8iUDXPCI3UL0DAcg/videos

Null profile- https://null.co.in/profile/20680-raunak-parmar
