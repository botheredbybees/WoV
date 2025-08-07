CREATE OR REPLACE VIEW wov.ebird_checklist_export AS
SELECT
    tax.scientific_name AS "Species",
    obs.group_size_estimate AS "Count",
    obs.observed_on AS "Date",
    obs.time_observed_at AS "Time",
    obs.latitude AS "Latitude",
    obs.longitude AS "Longitude",
    'RSV_Nuyina_' || vyg.name AS "Location",
    'Traveling' AS "Protocol",
    60 AS "Duration",
    3.5 AS "Effort Distance",
    usr.email AS "Observer",
    obs.description AS "Comments"
FROM
    wov.wov_observations obs
LEFT JOIN
    wov.wov_taxa tax ON obs.wov_taxa_id = tax.taxa_id
LEFT JOIN
    wov.wov_users usr ON obs.user_id = usr.user_id
LEFT JOIN
    wov.wov_voyages vyg ON obs.voyage_id = vyg.voyage_id;
