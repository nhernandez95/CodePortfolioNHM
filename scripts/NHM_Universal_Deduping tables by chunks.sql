-- © 2025 Nathanael Hernandez – Universal version
-- This SQL script has been sanitized to remove proprietary names and sensitive data.

-- Author: Nathanael H.
-- Date: 2025-03-05
-- This script is designed to deduplicate data from a source table and insert it into a new table in chunks of 7 days.
-- It uses a loop to process the data in manageable chunks, ensuring that the deduplication process is efficient and does not overload the system.
if OBJECT_ID('schema.table_deduped') is not null
    drop table schema.table_deduped;
Create schema.table_deduped as
Select top 0 * from schema.table; -- Create a new table with the same structure as the source table

-- Declare variables for chunk processing
DECLARE @StartDate DATE = '2021-03-26'; -- Start date of the data
DECLARE @EndDate DATE = GETDATE(); -- Current date
DECLARE @CurrentStartDate DATE;
DECLARE @CurrentEndDate DATE;

-- Loop through each month
SET @CurrentStartDate = @StartDate;
WHILE @CurrentStartDate <= @EndDate
BEGIN
    -- Set the end date for the current chunk (7 days later)
    SET @CurrentEndDate = DATEADD(DAY, 6, @CurrentStartDate);

    -- Insert deduplicated data for the current chunk into the new table
    INSERT INTO schema.table_deduped(columns...)
    SELECT distinct
           columns...
			from schema.table
    WHERE [ProcessingDate] BETWEEN @CurrentStartDate AND @CurrentEndDate;

    -- Move to the next chunk
    SET @CurrentStartDate = DATEADD(DAY, 1, @CurrentEndDate);
END;

-- Declare variables for chunk processing
DECLARE @StartDate DATE = '2021-03-26'; -- Start date of the data
DECLARE @EndDate DATE = GETDATE(); -- Current date
DECLARE @CurrentStartDate DATE;
DECLARE @CurrentEndDate DATE;

-- Loop through each month
SET @CurrentStartDate = @StartDate;
WHILE @CurrentStartDate <= @EndDate
BEGIN
    -- Set the end date for the current chunk (7 days later)
    SET @CurrentEndDate = DATEADD(DAY, 6, @CurrentStartDate);

    -- Insert deduplicated data for the current chunk into the new table
    INSERT INTO schema.table(columns...)
    SELECT distinct
           columns...
			from schema.table_deduped
    WHERE [ProcessingDate] BETWEEN @CurrentStartDate AND @CurrentEndDate;

    -- Move to the next chunk
    SET @CurrentStartDate = DATEADD(DAY, 1, @CurrentEndDate);
END;




