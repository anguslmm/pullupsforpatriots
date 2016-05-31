```
  __  __         _     _    
 |  \/  |___  __| |___| |___
 | |\/| / _ \/ _` / -_) (_-<
 |_|  |_\___/\__,_\___|_/__/
                            
```

This document details the structure of the models and their relationships.

It is currently formatted by my arbitrary standards. If anyone discovers a
better way to do this, please let me know and I'll change it.

## Marine
|Attribute   |Type      |Description                                           |
|------------|:--------:|-----------------------------------------------------:|
|Name        |String    |Name of the Marine
|AmountRaised|Decimal   |Amount raised in dollars, generated from donations

## Donation
|Attribute   |Type      |Description                                           |
|------------|:--------:|-----------------------------------------------------:|
|Marine      |ForeignKey|The Marine who's name it's donated in
|Amount      |Decimal   |Amount Donated
|Donor       |ForeignKey|The donor
|Message     |Text      |An optional message with the donation
|Public      |Boolean   |Should this donation be publicly viewable

## Donor
|Attribute   |Type      |Description                                           |
|------------|:--------:|-----------------------------------------------------:|
|Name        |String    |The name of the donor                                 |

## Sponsor
|Attribute   |Type      |Description                                           |
|------------|:--------:|-----------------------------------------------------:|
|Name        |String    |Name of the business or organization                  |
|LogoURL     |URL       |Url of the business or organization's logo            |
|Website     |URL       |Url of the business or organization's website         |
|Description |Text      |Description of the business or organization           |