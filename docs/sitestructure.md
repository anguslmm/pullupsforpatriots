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
/                       # Main splash screen
ourcause                # Info on the charity
contact                 # Contact infomation
donations               # All urls inside the fundraising app go after this
    ourgoal             # Goal with progress indicator
    marines/            # Shows top 10, search field, and link to full list
        search          # Search results for Marines
        all             # Paginated alphabetical list of marines
        :id             # Individual Marine's profile
    sponsors            # Show event sponsors
    donors              # Show donors with public donations
```

Indented urls mean that one goes after the other (like a folder inside another).
For example: The marines search page would be `donations/marines/search`