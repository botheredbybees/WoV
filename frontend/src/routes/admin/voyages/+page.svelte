<script>
    import { onMount } from 'svelte';

    let voyages = [];

    onMount(async () => {
        const response = await fetch('http://localhost:8004/voyages');
        voyages = await response.json();
    });
</script>

<h1>Manage Voyages</h1>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Region</th>
            <th>Start Date</th>
            <th>End Date</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {#each voyages as voyage}
            <tr>
                <td>{voyage.name}</td>
                <td>{voyage.region}</td>
                <td>{voyage.start_date}</td>
                <td>{voyage.end_date}</td>
                <td>
                    <a href="/admin/voyages/{voyage.voyage_id}">Edit</a>
                </td>
            </tr>
        {/each}
    </tbody>
</table>
