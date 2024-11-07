function additem() {
    const itemInput = document.getElementById("itemInput");
    const itemText = itemInput.value.trim();
  
    if (itemText) {
      const itemsList = document.getElementById("itemsList");
  
      // Create a new list item element
      const listItem = document.createElement("li");
      listItem.textContent = itemText;
  
      // Create a remove button for the list item
      const removeButton = document.createElement("button");
      removeButton.textContent = "Remove";
      removeButton.classList.add("remove");
  
      // Add an event listener to remove the item
      removeButton.addEventListener("click", function () {
        itemsList.removeChild(listItem);
      });
  
      // Append the remove button to the list item, and the item to the list
      listItem.appendChild(removeButton);
      itemsList.appendChild(listItem);
  
      // Clear the input field
      itemInput.value = "";
    } else {
      alert("Please enter an item.");
    }
  }
  