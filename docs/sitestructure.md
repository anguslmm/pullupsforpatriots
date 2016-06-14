```
  ___ _               _                
 / __| |_ _ _ _  _ __| |_ _  _ _ _ ___ 
 \__ \  _| '_| || / _|  _| || | '_/ -_)
 |___/\__|_|  \_,_\__|\__|\_,_|_| \___|
                                       
```

This document details the structure of the website.

It is currently formatted by my arbitrary standards. If anyone discovers a
better way to do this, please let me know and I'll change it.

```
/                           # Main splash screen with goal
ourcause/                   # Info on the charity  
fundraising/
    sponsors/               # Show event sponsors
    companyd/               # Shows top 10, search field, and link to full list
        search              # Search results for Marines
        all                 # Paginated alphabetical list of marines
        about               # About the command, contact info, etc
    niocga/                 # Shows top 10, search field, and link to full list
        search              # Search results for Sailors
        all                 # Paginated alphabetical list of sailors
        about               # About the command, contact info, etc.

```

Indented urls mean that one goes after the other (like a folder inside another).
For example: The marines search page would be `donations/marines/search`