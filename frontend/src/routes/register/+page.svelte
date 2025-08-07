<script>
	let email = '';
	let password = '';
	let confirmPassword = '';

	function handleSubmit() {
		if (password !== confirmPassword) {
			alert('Passwords do not match');
			return;
		}
		console.log('Registering with:', { email, password });
	}
</script>

<h1>Register</h1>

<form on:submit|preventDefault={handleSubmit}>
	<div>
		<label for="email">Email</label>
		<input id="email" name="email" type="email" bind:value={email} required />
	</div>
	<div>
		<label for="password">Password</label>
		<input id="password" name="password" type="password" bind:value={password} required />
	</div>
	<div>
		<label for="confirm-password">Confirm Password</label>
		<input
			id="confirm-password"
			name="confirm-password"
			type="password"
			bind:value={confirmPassword}
			required
		/>
	</div>
	<button type="submit">Register</button>
</form>

<style>
	form {
		display: flex;
		flex-direction: column;
		gap: 1rem;
		max-width: 300px;
	}
	div {
		display: flex;
		flex-direction: column;
	}
</style>
