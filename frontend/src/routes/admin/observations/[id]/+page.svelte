<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    let observation = {};
    let observationId = $page.params.id;

    onMount(async () => {
        const response = await fetch(`http://localhost:8004/observations/${observationId}`);
        observation = await response.json();
    });

    async function handleSubmit() {
        const response = await fetch(`http://localhost:8004/observations/${observationId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(observation)
        });

        if (response.ok) {
            alert('Observation updated successfully!');
        } else {
            alert('Failed to update observation.');
        }
    }
</script>

<h1>Edit Observation</h1>

<form on:submit|preventDefault={handleSubmit}>
    <div>
        <label for="species_guess">Species Guess</label>
        <input id="species_guess" type="text" bind:value={observation.species_guess} />
    </div>
    <div>
        <label for="common_name">Common Name</label>
        <input id="common_name" type="text" bind:value={observation.common_name} />
    </div>
    <div>
        <label for="observed_on">Observed On</label>
        <input id="observed_on" type="date" bind:value={observation.observed_on} />
    </div>
    <div>
        <label for="latitude">Latitude</label>
        <input id="latitude" type="number" bind:value={observation.latitude} />
    </div>
    <div>
        <label for="longitude">Longitude</label>
        <input id="longitude" type="number" bind:value={observation.longitude} />
    </div>
    <div>
        <label for="notes">Notes</label>
        <textarea id="notes" bind:value={observation.description}></textarea>
    </div>
    <button type="submit">Save</button>
</form>
