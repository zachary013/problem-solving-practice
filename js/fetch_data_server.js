// Function to simulate fetching data from a server with a delay
function fetchData() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        const data = [
          { id: 1, name: 'John Doe', age: 32 },
          { id: 2, name: 'Jane Smith', age: 27 },
          { id: 3, name: 'Sam Williams', age: 45 },
        ];
        const isError = false;  // Simulate an error condition
        if (!isError) {
          resolve(data);
        } else {
          reject('Error: Failed to fetch data');
        }
      }, 2000); // Simulate 2-second delay
    });
  }
  
  // Function to process and display the fetched data
  async function processData() {
    try {
      const data = await fetchData(); // Wait for data fetching
      // Filter users older than 30
      const filteredData = data.filter(user => user.age > 30);
      // Map the filtered data to a new format
      const formattedData = filteredData.map(user => ({
        fullName: user.name,
        yearsOld: user.age,
      }));
      console.log('Processed Data:', formattedData); // Log the processed data
    } catch (error) {
      console.error(error); // Handle any errors
    }
  }
  
  processData();  // Execute the function
  