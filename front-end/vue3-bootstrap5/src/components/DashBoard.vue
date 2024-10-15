<template>
    <div>
        <!-- Navigation Bar -->
        <nav class="navbar navbar-expand-lg navbar-light fixed-top py-3 navbar-shrink" id="mainNav">
            <div class="container-fluid">
                <a class="navbar-brand" href="#page-top">Probless</a>
                <button class="navbar-toggler navbar-toggler-right" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
                    aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto my-2 my-lg-0">
                        <li class="nav-item"><a class="nav-link" href="#about">Home</a></li>
                        <li class="nav-item"><a class="nav-link active" href="#services">Dashboard</a></li>
                        <li class="nav-item"><a class="nav-link" href="#portfolio">Settings</a></li>
                        <li class="nav-item"><a class="nav-link" href="#contact">Profile</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Main Dashboard Content -->
        <div class="container-fluid mt-5 pt-5">
            <img @click="toggleSidebar"
                src="https://icons.veryicon.com/png/o/miscellaneous/godserver/expand-sidebar.png" alt="Toggle Sidebar"
                class="sidebar-toggle-icon mb-3" />

            <div class="row">
                <!-- Sidebar -->
                <div v-if="isSidebarVisible" class="col-md-1 bg-light sidebar">
                    <ul class="list-group">
                        <li class="list-group-item"><a href="#">My Tickets</a></li>
                        <li class="list-group-item"><a href="#">Ticket History</a></li>
                        <li class="list-group-item"><a href="#">User Management</a></li>
                        <li class="list-group-item"><a href="#">.....</a></li>
                    </ul>
                </div>

                <!-- Main Content Area -->
                <div :class="isSidebarVisible ? 'col-md-9' : 'col-md-12'">
                    <div class="row">
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">Open tickets</h5>
                                    <p class="card-text">No open tickets...</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">Resolved tickets</h5>
                                    <p class="card-text">No tickets had been solved...</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 mb-3">
                            <div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">Pending Tickets</h5>
                                    <p class="card-text">No tickets pending...</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Create Ticket Button -->
                    <button class="btn btn-danger create-ticket-button" @click="showModal = true">
                        Create Ticket
                    </button>
                </div>
            </div>
        </div>

        <!-- Create Ticket Modal -->
        <div v-if="showModal" class="modal-overlay">
            <div class="modal-content">
                <h5>Create a New Ticket</h5>
                <form @submit.prevent="createTicket">
                    <div class="mb-3">
                        <label for="title" class="form-label">Title</label>
                        <input type="text" id="title" v-model="ticket.title" class="form-control">
                    </div>
                    <div class="mb-3">
                        <label for="description" class="form-label">Description</label>
                        <textarea id="description" v-model="ticket.description" class="form-control"></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="priority" class="form-label">Priority</label>
                        <select id="priority" v-model="ticket.priority" class="form-select">
                            <option>Low</option>
                            <option>Medium</option>
                            <option>High</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="department" class="form-label">Department</label>
                        <input type="text" id="department" v-model="ticket.department" class="form-control">
                    </div>
                    <button type="submit" class="btn btn-danger">Create</button>
                    <button type="button" class="btn btn-secondary" @click="showModal = false">Cancel</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isSidebarVisible: true, // Controls sidebar visibility
            showModal: false, // Controls modal visibility
            ticket: {
                title: '',
                description: '',
                priority: 'Low',
                department: ''
            }
        };
    },
    methods: {
        toggleSidebar() {
            this.isSidebarVisible = !this.isSidebarVisible;
        },
        createTicket() {
            console.log('Ticket created:', this.ticket);
            this.showModal = false; // Close the modal after ticket creation
        }
    }
};
</script>

<style>
/* Sidebar styles */
.sidebar {
    height: 100vh;
    position: sticky;
    top: 0;
    font-size: smaller;
    transition: all 0.3s ease;
}

.sidebar-toggle-icon {
    width: 40px;
    /* Adjust the size as needed */
    height: 40px;
    cursor: pointer;
    transition: transform 0.2s ease;
}

/* Create Ticket Button Styles */
.create-ticket-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
}

/* Modal Overlay Styles */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10000;
}

/* Modal Content Styles */
.modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 400px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}
</style>
