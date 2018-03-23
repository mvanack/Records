#!/usr/bin/env python

import toyplot
import requests
import pandas as pd

baseurl = "http://api.gbif.org/v1/occurrence/search?"


# initialized object calls the request and returns a full dataframe from GBIF
# q is species and interval is year interval

class Records:


    def __init__(self, q=None, interval=None):

        gbif_interval = str(interval[0]) + "," + str(interval[1])

        self.q = q
        self.interval = interval
        self.params = {
            "year": gbif_interval,
            "q": self.q,
            "basisOfRecord": "PRESERVED_SPECIMEN",
            "hasCoordinate": "true",
            "hasGeospatialIssue": "false",
            "country": "US",
            "offset": "0",
            "limit": "300"
        }
        self.df = self.get_all_records()

    def get_all_records(self):
        "iterate until end of records"
        start = 0
        data = []  # start with empty list to keep filling until end of query

        while 1:  # while 1 is same as while TRUE
            # make request and store results
            res = requests.get(
                url=baseurl,
                params=self.params,
            )
            temp_params = self.params
        # increment counter
            temp_params["offset"] = str(int(temp_params["offset"]) + 300)

        # concatenate data
            idata = res.json()
            data += idata["results"]

            # stop when end of record is reached
            if idata["endOfRecords"]:
                break
        # convert to a data frame
        df = pd.DataFrame(data)
        return df

        