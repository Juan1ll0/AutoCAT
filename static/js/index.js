function serveFeed(e) {
   console.log("js serve feed")
  fetch( `/serveFeed`)
  .then( response => {
    console.log(response);
  } )
}

function convertUtcToLocalTime(utcTimeStr) {
    // Parse the input string
    const [utcHours, utcMinutes] = utcTimeStr.split(':').map(Number);

    // Create a Date object in UTC
    const date = new Date(Date.UTC(new Date().getUTCFullYear(), new Date().getUTCMonth(), new Date().getUTCDate(), utcHours, utcMinutes));

    // Get the local time components
    const localHours = date.getHours();
    const localMinutes = date.getMinutes();

    // Format the local time as HH:MM
    const formattedLocalTime = `${localHours.toString().padStart(2, '0')}:${localMinutes.toString().padStart(2, '0')}`;

    return formattedLocalTime;
}

 async function submitForm(event) {
        event.preventDefault();  // Prevent the default form submission

        // Collect form data
        const form = event.target;
        const data = [];

        const nameInputs = form.querySelectorAll('input[name="meal"]');
        const timeInputs = form.querySelectorAll('input[name="time"]');
        const quantityInputs = form.querySelectorAll('input[name="quantity"]');

        for (let i = 0; i < timeInputs.length; i++) {
            const hour = {
                name: nameInputs[i].value,
                time: timeInputs[i].value,
                quantity: parseInt(quantityInputs[i].value,10)
            };
            data.push(hour);
        }

        // Send data as JSON
        const response = await fetch('/setScheduler', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            alert('Scheduler set successfully');
        } else {
            alert('Error setting scheduler');
        }
    }
