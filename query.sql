SELECT 
	radacct.radacctid,
--     convert(radacct.acctsessionid, char) AS acctsessionid,
--     convert(radacct.acctuniqueid, char) AS acctuniqueid,
--     convert(radacct.username, char) AS username,
	inet_ntoa(radacct.nasipaddress) AS nasipaddress,
--     radacct.nasporttype,
    from_unixtime(radacct.acctstarttime) AS acctstarttime,
    -- from_unixtime(radacct.acctupdatetime) AS acctupdatetime,
    from_unixtime(radacct.acctstoptime) AS acctstoptime,
    radacct.acctinputoctets,
    radacct.acctoutputoctets,
    convert(radacct.calledstationid, char) AS calledstationid,
    concat(radacct.cc, radacct.npa,radacct.sn) AS msisdn,
--     (SELECT tc.value FROM terminate_cause_index tc
-- 		WHERE tc.id = radacct.acctterminatecause) AS acctterminatecause,
    inet_ntoa(radacct.framedipaddress) AS framedipaddress,
    radacct.mcc,
    convert(radacct.mnc, char) AS mnc,
    radacct.lac,
    radacct.cellid
FROM radius_transmeet.radacct WHERE concat(cc, npa, sn) = 'MSISDN' 
ORDER BY radacctid DESC LIMIT 10;
