# PowerShell script to list out those that have departed

$version = '0.1.0'

# User data.  Name and last day.     

$json1 = @"
{
"Zombie":
    [
        {
            "Name": "User1",
            "Expiration": "2015-05-12"
        },
        {
            "Name": "User2",
            "Expiration": "2015-08-05"
        },
        {
            "Name": "User3",
            "Expiration": "2014-08-28"
        },
        {
            "Name": "User4",
            "Expiration": "2015-08-18"
        },
        {
            "Name": "User5",
            "Expiration": "2014-11-22"
        },
        {
            "Name": "User6",
            "Expiration": "2015-01-14"
        },
        {
            "Name": "User7",
            "Expiration": "2016-03-05"
        }
    ]
}
"@      

# Convert json to MS Object
$msjson = $json1 | convertFrom-json

$zCount = 0
$Total_Zombies =$msjson.zombie.count
#$zCount
write-host "Zombie"
write-host $version "`n"
write-output $version
get-date
write-host "Total Zombies:" $Total_Zombies
do {    
        $results = (get-date) - (get-date $msjson.Zombie[$zCount].Expiration)
        write-host $msjson.zombie[$zCount].name "Days:`t"$results.days 
        $zCount++
    } while ($zCount -lt $Total_Zombies)