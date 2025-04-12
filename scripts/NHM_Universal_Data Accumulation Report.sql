-- © 2025 Nathanael Hernandez – Universal version
-- This SQL script has been sanitized to remove proprietary names and sensitive data.

--By Nathanael Hernandez
-- Date: 2023-10-03
-- Description: This script retrieves the last report date and calculates various fees based on the data in the [DBO].[DataAccumulation] table.
declare @lastReportDate date
set @lastReportDate = (select max(DateOfReport) from [DBO].[DataAccumulation]);
select
    TIN,
    case
        when tbl1AVolume>0 then 'Y'
        else ''
    end as tbl1A,
    case
        when tbl1BVolume>0 then 'Y'
        else ''
    end as tbl1B,
    case
        when tbl2Volume>0 then 'Y'
        else ''
    end as tbl2,
    tbl1AVolume,
    tbl1ATier,
    tbl1AFee,
    [CP Table 1a or 1b],
    tbl1BVolume,
    tbl1BTier,
    tbl1BFee,
    tbl2Volume,
    tbl2Tier,
    tbl2Fee,
    tbl1AFee+tbl1BFee+tbl2Fee as TotalFee,
    ReportDate as FileDate,
	eomonth(dateadd(m,-1,ReportDate)) as ReportDate
from(
	select distinct
        convert(bigint,TIN) as TIN,
        case
            when [CPTable1aOr1b]='1a' then CardPresent
            else 0.00
        end as tbl1AVolume,
        case
            when [CPTable1aOr1b]='1a' then CPTableTier
            else ''
        end as tbl1ATier,
        case
            when [CPTable1aOr1b]='1a' then Permerchant_idFANFCostForCPFor1month
            else 0.00
        end as tbl1AFee,
        CPTable1aOr1b as [CP Table 1a or 1b],
        case
            when [CPTable1aOr1b]='1b' or CardPresent>0 then CardPresent
            else 0.00
        end as tbl1BVolume,
        case
            when [CPTable1aOr1b]='1b' then CPTableTier
            else ''
        end as tbl1BTier,
        case
            when [CPTable1aOr1b]='1b' then Permerchant_idFANFCostForCPFor1month
            else 0.00
        end as tbl1BFee,
        CardNotPresent as tbl2Volume,
        Table2Tier as tbl2Tier,
        Permerchant_idFANFCostCorCNPFor1month as tbl2Fee,
        DateOfReport as ReportDate
    from
        [DBO].[DataAccumulation]
    where DateOfReport = @lastReportDate  and TIN is not null) a
order by a.ReportDate,a.TIN
