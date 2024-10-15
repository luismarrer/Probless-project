<template>
    <div>
        <!-- Modal (Appears when showModal is true) -->
        <div v-if="showModal" class="modal-overlay">
            <div class="modal-content">
                <h3>Create a Ticket</h3>

                <!-- Form for Ticket Details -->
                <form @submit.prevent="submitTicket">
                    <div class="mb-3">
                        <label for="title" class="form-label">Title</label>
                        <input type="text" id="title" v-model="ticket.title" class="form-control" required>
                    </div>

                    <div class="mb-3">
                        <label for="description" class="form-label">Description</label>
                        <textarea id="description" v-model="ticket.description" class="form-control"
                            required></textarea>
                    </div>

                    <div class="mb-3">
                        <label for="priority" class="form-label">Priority</label>
                        <select id="priority" v-model="ticket.priority" class="form-select" required>
                            <option value="low">Low</option>
                            <option value="medium">Medium</option>
                            <option value="high">High</option>
                        </select>
                    </div>

                    <div class="mb-3">
                        <label for="department" class="form-label">Department</label>
                        <select id="department" v-model="ticket.department" class="form-select" required>
                            <option value="IT">IT</option>
                            <option value="HR">HR</option>
                            <option value="Finance">Finance</option>
                        </select>
                    </div>

                    <button type="submit" class="btn btn-danger">Create</button>
                    <button type="button" class="btn btn-secondary" @click="closeModal">Cancel</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showModal: false, // Control modal visibility
            ticket: {
                title: '',
                description: '',
                priority: '',
                department: '',
            },
        };
    },
    methods: {
        closeModal() {
            this.showModal = false; // Close the modal
        },
        submitTicket() {
            // Handle form submission logic here
            console.log('Ticket submitted:', this.ticket);
            this.closeModal(); // Close the modal after submission
        },
    },
};
</script>

<style scoped>
/* Modal Styles */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    /* Blurry background */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    width: 400px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

body.modal-open {
    overflow: hidden;
    /* Prevent background scrolling */
}
</style>