const notificationswal = (titleText, text, icon, confirmButtonText) => {
    swal.fire({
        titleText: titleText,
        text: text,
        icon: icon,
        confirmButtonText: confirmButtonText,
    });
};