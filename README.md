# Description
This tool will enumerate all the URL's in the file and will classify all of them according to their content-Length, Status-code, Title, Server, Forms, possbile Dom-XSS.
Result will be saved in different files in given foldername
This tool makes easy to select the targets when you have lot's of domains to enumerate

There are 2 codeza.py one is for python2 and another one is for python3

### [Watch video](https://twitter.com/trouble1_raunak/status/1223649330562600960?s=09)

```
 ____________________________________________________________________
|           /|                                                       |
|          / |                                                       |
|    _____|  |_____                                                  |      
|   /_____   _____/                                                  |
|         |  | _      ____   ____   ____   _____  _____      _       |    
|         |  || |    |####| |####| |####  |##### |#####     /#\      |    
|         |  || |   |#      #    # |#   # |#|___    /#     /# #\     |    
|         |  || |   |#      #    # |#   # |####    /#     /#/_\#\    |    
|         |  ||/    |#____  #____# |#___# |#|__   /#___  /#/   \#\   |    
|         | /        |####| |####| |####  |##### /##### /#/     \#\  |    
|         |/                                                         |    
|                     # Coded By Raunak Parmar - @trouble1_raunak    |
|____________________________________________________________________|
```

![Image codeza](https://github.com/TROUBLE-1/codeza/blob/master/Images/7.JPG)

# Note
I have provided a list of subdomins of \*.ford.com with more then 5000 domins.

Provide file_name, min_content_length, Folder_name_to_create respectively while using codeza.py

Make sure file contains URL's with http:// or https://

# Installing modules
```
sudo pip install -r requirements.txt
```

# Usage
1. Get all list of subdomains in a file (eg. all.txt)
2. use httprobe command (eg. cat all.txt | httprobe > alive.txt) --> https://github.com/tomnomnom/httprobe
  Now Use codeza.py to enumerate all url's
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

Nullmeet profile- https://null.co.in/profile/20680-raunak-parmar

# Images

![Image codeza](https://github.com/TROUBLE-1/codeza/blob/master/Images/1.JPG)

![Image codeza](https://github.com/TROUBLE-1/codeza/blob/master/Images/2.JPG)

![Image codeza](https://github.com/TROUBLE-1/codeza/blob/master/Images/3.JPG)

![Image codeza](https://github.com/TROUBLE-1/codeza/blob/master/Images/4.JPG)

![Image codeza](https://github.com/TROUBLE-1/codeza/blob/master/Images/5.JPG)

![Image codeza](https://github.com/TROUBLE-1/codeza/blob/master/Images/6.JPG)
