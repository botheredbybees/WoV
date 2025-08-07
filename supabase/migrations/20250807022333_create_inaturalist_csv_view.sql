CREATE OR REPLACE VIEW wov.inaturalist_csv_export AS
SELECT
    obs.observed_on,
    obs.time_observed_at,
    tax.scientific_name,
    tax.common_name,
    obs.latitude,
    obs.longitude,
    obs.description,
    img.file_path AS "image_url",
    'true' AS "id_please",
    'voyage:' || obs.voyage_id AS "tag_list",
    'false' AS "captive_cultivated",
    'sea_state=' || obs.sea_surface_temp || ';wind_speed=' || obs.wind_speed_true || ';air_temp=' || obs.air_temp AS "observation_fields"
FROM
    wov.wov_observations obs
LEFT JOIN
    wov.wov_taxa tax ON obs.wov_taxa_id = tax.taxa_id
LEFT JOIN
    wov.wov_images img ON obs.observation_id = img.observation_id;
