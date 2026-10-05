document.addEventListener('DOMContentLoaded', () => {
    // === Dark Mode Toggle ===
    const themeToggleBtn = document.getElementById('theme-toggle');
    const darkIcon = document.getElementById('theme-toggle-dark-icon');
    const lightIcon = document.getElementById('theme-toggle-light-icon');

    // Check preference
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
        if (darkIcon) darkIcon.classList.remove('hidden');
    } else {
        document.documentElement.classList.remove('dark');
        if (lightIcon) lightIcon.classList.remove('hidden');
    }

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            darkIcon.classList.toggle('hidden');
            lightIcon.classList.toggle('hidden');

            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            }
        });
    }

    // === Sidebar Mobile Toggle ===
    const openSidebarBtn = document.getElementById('open-sidebar');
    const closeSidebarBtn = document.getElementById('close-sidebar');
    const sidebar = document.getElementById('sidebar');
    const mobileOverlay = document.getElementById('mobile-overlay');

    function toggleSidebar() {
        if (!sidebar) return;
        
        if (sidebar.classList.contains('-translate-x-full')) {
            // Open
            sidebar.classList.remove('-translate-x-full');
            mobileOverlay.classList.remove('hidden');
            document.body.classList.add('overflow-hidden');
        } else {
            // Close
            sidebar.classList.add('-translate-x-full');
            mobileOverlay.classList.add('hidden');
            document.body.classList.remove('overflow-hidden');
        }
    }

    if (openSidebarBtn) openSidebarBtn.addEventListener('click', toggleSidebar);
    if (closeSidebarBtn) closeSidebarBtn.addEventListener('click', toggleSidebar);
    if (mobileOverlay) mobileOverlay.addEventListener('click', toggleSidebar);

    // === Toasts Auto-Dismiss ===
    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(toast => {
        setTimeout(() => {
            toast.classList.add('hiding');
            setTimeout(() => {
                toast.remove();
            }, 300); // Wait for fade out animation
        }, 4000); // 4 seconds
    });

    // === Close dropdowns when clicking outside ===
    document.addEventListener('click', (e) => {
        const dropdowns = document.querySelectorAll('.dropdown-menu');
        dropdowns.forEach(menu => {
            if (!menu.classList.contains('hidden') && !menu.parentElement.contains(e.target)) {
                menu.classList.add('hidden');
            }
        });
    });
});

// === Modals and Dropdowns Logic ===

window.toggleDropdown = function(id, event) {
    if (event) {
        event.stopPropagation();
    }
    const menu = document.getElementById(id);
    
    // Close other dropdowns
    document.querySelectorAll('.dropdown-menu').forEach(m => {
        if (m.id !== id && !m.classList.contains('hidden')) {
            m.classList.add('hidden');
        }
    });

    if (menu) {
        menu.classList.toggle('hidden');
    }
};

window.openModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('hidden');
        // Simple animation classes could be added here
        document.body.style.overflow = 'hidden'; // Prevent scrolling background
    }
};

window.closeModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('hidden');
        document.body.style.overflow = '';
    }
};

window.openEditModal = function(id, title, description, category, priority, dueDate) {
    // Populate form fields
    const form = document.getElementById('editTaskForm');
    if (form) {
        // We use window.location.origin to build the URL dynamically but Django forms submit to the specific action.
        // It's better to update action URL. Let's just set the action attribute.
        form.action = `/task/${id}/edit/`;
    }
    
    document.getElementById('edit-title').value = title || '';
    document.getElementById('edit-description').value = description || '';
    document.getElementById('edit-category').value = category || 'Personal';
    document.getElementById('edit-priority').value = priority || 'Medium';
    document.getElementById('edit-due-date').value = dueDate || '';
    
    openModal('editTaskModal');
};

window.openDeleteModal = function(id) {
    const form = document.getElementById('deleteTaskForm');
    if (form) {
        form.action = `/task/${id}/delete/`;
    }
    openModal('deleteTaskModal');
};

window.openEditModalFromElement = function(el) {
    const id = el.getAttribute('data-id');
    const title = el.getAttribute('data-title');
    const desc = el.getAttribute('data-desc');
    const category = el.getAttribute('data-category');
    const priority = el.getAttribute('data-priority');
    const due = el.getAttribute('data-due');
    window.openEditModal(id, title, desc, category, priority, due);
};
