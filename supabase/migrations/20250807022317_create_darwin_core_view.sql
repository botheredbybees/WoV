CREATE OR REPLACE VIEW wov.darwin_core_export AS
SELECT
    obs.voyage_id || ':obs-' || obs.observation_id AS "eventID",
    'obs-' || obs.observation_id AS "occurrenceID",
    'HumanObservation' AS "basisOfRecord",
    tax.scientific_name AS "scientificName",
    tax.taxonomy_class AS "taxonRank",
    tax.inaturalist_taxa_id AS "taxonID",
    obs.observed_on AS "eventDate",
    obs.time_observed_at AS "eventTime",
    EXTRACT(DOY FROM obs.observed_on) AS "startDayOfYear",
    obs.latitude AS "decimalLatitude",
    obs.longitude AS "decimalLongitude",
    obs.positional_accuracy AS "coordinateUncertaintyInMeters",
    usr.username AS "identifiedBy",
    usr.username AS "recordedBy",
    obs.group_size_estimate AS "individualCount",
    NULL AS "sex",
    NULL AS "lifeStage",
    NULL AS "behavior",
    obs.description AS "occurrenceRemarks",
    'present' AS "occurrenceStatus",
    obs.license,
    'AAD' AS "institutionCode",
    'WOV Observations' AS "dataProviderName",
    'RV Nuyina 2025 log' AS "dataResourceName",
    'WGS84' AS "geodeticDatum",
    NULL AS "locationRemarks",
    img.file_path AS "associatedMedia"
FROM
    wov.wov_observations obs
LEFT JOIN
    wov.wov_taxa tax ON obs.wov_taxa_id = tax.taxa_id
LEFT JOIN
    wov.wov_users usr ON obs.user_id = usr.user_id
LEFT JOIN
    wov.wov_images img ON obs.observation_id = img.observation_id;
