<script>
    import { onMount } from 'svelte';

    let users = [];

    onMount(async () => {
        const response = await fetch('http://localhost:8004/users');
        users = await response.json();
    });
</script>

<h1>Manage Users</h1>

<table>
    <thead>
        <tr>
            <th>Username</th>
            <th>Email</th>
            <th>Role</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {#each users as user}
            <tr>
                <td>{user.username}</td>
                <td>{user.email}</td>
                <td>{user.role}</td>
                <td>
                    <a href="/admin/users/{user.user_id}">Edit</a>
                </td>
            </tr>
        {/each}
    </tbody>
</table>
