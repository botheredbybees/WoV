<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    let voyage = {};
    let voyageId = $page.params.id;

    onMount(async () => {
        const response = await fetch(`http://localhost:8004/voyages/${voyageId}`);
        voyage = await response.json();
    });

    async function handleSubmit() {
        const response = await fetch(`http://localhost:8004/voyages/${voyageId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(voyage)
        });

        if (response.ok) {
            alert('Voyage updated successfully!');
        } else {
            alert('Failed to update voyage.');
        }
    }
</script>

<h1>Edit Voyage</h1>

<form on:submit|preventDefault={handleSubmit}>
    <div>
        <label for="name">Name</label>
        <input id="name" type="text" bind:value={voyage.name} />
    </div>
    <div>
        <label for="region">Region</label>
        <input id="region" type="text" bind:value={voyage.region} />
    </div>
    <div>
        <label for="start_date">Start Date</label>
        <input id="start_date" type="date" bind:value={voyage.start_date} />
    </div>
    <div>
        <label for="end_date">End Date</label>
        <input id="end_date" type="date" bind:value={voyage.end_date} />
    </div>
    <div>
        <label for="notes">Notes</label>
        <textarea id="notes" bind:value={voyage.notes}></textarea>
    </div>
    <button type="submit">Save</button>
</form>
