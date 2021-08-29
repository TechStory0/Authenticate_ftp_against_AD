Get-ADUser -Filter * -SearchBase "OU=test,DC=techstory,DC=local" -Properties * | Select-Object sAMAccountName | export-csv -path \\10.10.10.122\scripts\userexport.csv
