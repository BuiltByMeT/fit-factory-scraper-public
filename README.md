# Fit Factory Current Capacity Scraper
scrape the current capacity at local Fit Factory looking for low volume times to go

# IMPORTANT
steps before committing:

adjust [user] in filename (myscraper.py) before and after committing b/c privacy reasons

-----------------------------------------------------------------------------------------

### set up cronjobs
```
$ crontab -e
```
```
# every 30 minutes between 5-7 AM Monday-Friday
*/30 5-7 * * 1-5 /usr/bin/python3  ~/Documents/projects/BuiltByMeT/scraper/fit-factory-scraper/myscraper.py
# every 30 minutes between 7AM-6PM Saturday and Sunday
*/30 7-18 * * 6,0 /usr/bin/python3  ~/Documents/projects/BuiltByMeT/scraper/fit-factory-scraper/myscraper.py
```
shutdown after scripts finish (has to be sudo to run shutdown commands)
```
$ sudo crontab -e
```
```
# shut down after scrape scripts run M-F    
31 7 * * 1-5 /sbin/shutdown -h now
# shut down after scrape scripts run Sat,Sun
31 18 * * 6,0 /sbin/shutdown -h now
```


### set up rtcwake to wake up computer at 04:59 every morning to run the cronjobs

manually enter for now and needs sudo to run rtcwake command

Sun night - Thur night
```
$ sudo rtcwake -m no -l -t $(date +%s -d 'tomorrow 04:59')
```

Fri & Sat night
```
$ sudo rtcwake -m no -l -t $(date +%s -d 'tomorrow 06:59')
```