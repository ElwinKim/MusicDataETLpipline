```python
%load_ext sql
```


```python
%sql postgresql://student:student123@127.0.0.1/sparkifydb
```


```python
%sql SELECT * FROM songplays LIMIT 5;
```

     * postgresql://student:***@127.0.0.1/sparkifydb
    5 rows affected.





<table>
    <tr>
        <th>songplay_id</th>
        <th>start_time</th>
        <th>user_id</th>
        <th>level</th>
        <th>song_id</th>
        <th>artist_id</th>
        <th>session_id</th>
        <th>location</th>
        <th>user_agent</th>
    </tr>
    <tr>
        <td>0</td>
        <td>1541721977796</td>
        <td>42</td>
        <td>paid</td>
        <td>None</td>
        <td>None</td>
        <td>275</td>
        <td>New York-Newark-Jersey City, NY-NJ-PA</td>
        <td>&quot;Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36&quot;</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1541722186796</td>
        <td>42</td>
        <td>paid</td>
        <td>None</td>
        <td>None</td>
        <td>275</td>
        <td>New York-Newark-Jersey City, NY-NJ-PA</td>
        <td>&quot;Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36&quot;</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1541722347796</td>
        <td>42</td>
        <td>paid</td>
        <td>None</td>
        <td>None</td>
        <td>275</td>
        <td>New York-Newark-Jersey City, NY-NJ-PA</td>
        <td>&quot;Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36&quot;</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1541722492796</td>
        <td>42</td>
        <td>paid</td>
        <td>None</td>
        <td>None</td>
        <td>275</td>
        <td>New York-Newark-Jersey City, NY-NJ-PA</td>
        <td>&quot;Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36&quot;</td>
    </tr>
    <tr>
        <td>4</td>
        <td>1541722664796</td>
        <td>42</td>
        <td>paid</td>
        <td>None</td>
        <td>None</td>
        <td>275</td>
        <td>New York-Newark-Jersey City, NY-NJ-PA</td>
        <td>&quot;Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36&quot;</td>
    </tr>
</table>




```python
%sql SELECT * FROM users LIMIT 5;
```

     * postgresql://student:***@127.0.0.1/sparkifydb
    5 rows affected.





<table>
    <tr>
        <th>user_id</th>
        <th>first_name</th>
        <th>last_name</th>
        <th>gender</th>
        <th>level</th>
    </tr>
    <tr>
        <td>42</td>
        <td>Harper</td>
        <td>Barrett</td>
        <td>M</td>
        <td>paid</td>
    </tr>
    <tr>
        <td>49</td>
        <td>Chloe</td>
        <td>Cuevas</td>
        <td>F</td>
        <td>free</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Cecilia</td>
        <td>Owens</td>
        <td>F</td>
        <td>free</td>
    </tr>
    <tr>
        <td>24</td>
        <td>Layla</td>
        <td>Griffin</td>
        <td>F</td>
        <td>paid</td>
    </tr>
    <tr>
        <td>80</td>
        <td>Tegan</td>
        <td>Levine</td>
        <td>F</td>
        <td>paid</td>
    </tr>
</table>




```python
%sql SELECT * FROM songs LIMIT 5;
```

     * postgresql://student:***@127.0.0.1/sparkifydb
    5 rows affected.





<table>
    <tr>
        <th>song_id</th>
        <th>artist_id</th>
        <th>title</th>
        <th>year</th>
        <th>duration</th>
    </tr>
    <tr>
        <td>SONHOTT12A8C13493C</td>
        <td>AR7G5I41187FB4CE6C</td>
        <td>Something Girls</td>
        <td>1982</td>
        <td>233.40363</td>
    </tr>
    <tr>
        <td>SOHKNRJ12A6701D1F8</td>
        <td>AR10USD1187B99F3F1</td>
        <td>Drop of Rain</td>
        <td>0</td>
        <td>189.57016</td>
    </tr>
    <tr>
        <td>SOUDSGM12AC9618304</td>
        <td>ARNTLGG11E2835DDB9</td>
        <td>Insatiable (Instrumental Version)</td>
        <td>0</td>
        <td>266.39628</td>
    </tr>
    <tr>
        <td>SOCIWDW12A8C13D406</td>
        <td>ARMJAGH1187FB546F3</td>
        <td>Soul Deep</td>
        <td>1969</td>
        <td>148.03546</td>
    </tr>
    <tr>
        <td>SOFSOCN12A8C143F5D</td>
        <td>ARXR32B1187FB57099</td>
        <td>Face the Ashes</td>
        <td>2007</td>
        <td>209.60608</td>
    </tr>
</table>




```python
%sql SELECT * FROM artists LIMIT 5;
```

     * postgresql://student:***@127.0.0.1/sparkifydb
    5 rows affected.





<table>
    <tr>
        <th>artist_id</th>
        <th>name</th>
        <th>location</th>
        <th>latitude</th>
        <th>longitude</th>
    </tr>
    <tr>
        <td>AR7G5I41187FB4CE6C</td>
        <td>Adam Ant</td>
        <td>London, England</td>
        <td>NaN</td>
        <td>NaN</td>
    </tr>
    <tr>
        <td>AR10USD1187B99F3F1</td>
        <td>Tweeterfriendly Music</td>
        <td>Burlington, Ontario, Canada</td>
        <td>NaN</td>
        <td>NaN</td>
    </tr>
    <tr>
        <td>ARNTLGG11E2835DDB9</td>
        <td>Clp</td>
        <td></td>
        <td>NaN</td>
        <td>NaN</td>
    </tr>
    <tr>
        <td>ARMJAGH1187FB546F3</td>
        <td>The Box Tops</td>
        <td>Memphis, TN</td>
        <td>35.14968</td>
        <td>-90.04892</td>
    </tr>
    <tr>
        <td>ARXR32B1187FB57099</td>
        <td>Gob</td>
        <td></td>
        <td>NaN</td>
        <td>NaN</td>
    </tr>
</table>




```python
%sql SELECT * FROM times LIMIT 5;
```

     * postgresql://student:***@127.0.0.1/sparkifydb
    5 rows affected.





<table>
    <tr>
        <th>start_time</th>
        <th>hour</th>
        <th>day</th>
        <th>week</th>
        <th>month</th>
        <th>year</th>
        <th>weekday</th>
    </tr>
    <tr>
        <td>1541721977796</td>
        <td>0</td>
        <td>9</td>
        <td>45</td>
        <td>11</td>
        <td>2018</td>
        <td>4</td>
    </tr>
    <tr>
        <td>1541722186796</td>
        <td>0</td>
        <td>9</td>
        <td>45</td>
        <td>11</td>
        <td>2018</td>
        <td>4</td>
    </tr>
    <tr>
        <td>1541722347796</td>
        <td>0</td>
        <td>9</td>
        <td>45</td>
        <td>11</td>
        <td>2018</td>
        <td>4</td>
    </tr>
    <tr>
        <td>1541722492796</td>
        <td>0</td>
        <td>9</td>
        <td>45</td>
        <td>11</td>
        <td>2018</td>
        <td>4</td>
    </tr>
    <tr>
        <td>1541722664796</td>
        <td>0</td>
        <td>9</td>
        <td>45</td>
        <td>11</td>
        <td>2018</td>
        <td>4</td>
    </tr>
</table>


```python

```
