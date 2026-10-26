
const button = document.getElementById("loadBuses");
const container = document.getElementById("busContainer");
const message = document.getElementById("message");

button.addEventListener("click", async () => {
    container.innerHTML = "";
    message.textContent = "Loading buses...";

    try {
        const response = await fetch("/buses");

        if (!response.ok) {
            throw new Error("Failed to retrieve buses");
        }

        const buses = await response.json();

        message.textContent = buses.length
            ? ""
            : "No buses available.";

        buses.forEach(bus => {
            const card = document.createElement("div");
            card.className = "bus-card";

            const heading = document.createElement("h3");
            heading.textContent = bus.bus_number;

            const type = document.createElement("p");
            type.textContent = "Type: " + bus.bus_type;

            const seats = document.createElement("p");
            seats.textContent = "Seats: " + bus.total_seats;

            const status = document.createElement("p");
            status.textContent = "Status: " + bus.status;

            card.append(heading, type, seats, status);
            container.appendChild(card);
        });

    } catch (error) {
        message.textContent =
            "Unable to load buses. Check the Flask server.";
        console.error(error);
    }
});






/* ROUTES SECTION */

const routeButton = document.getElementById("loadRoutes");
const routeContainer = document.getElementById("routeContainer");
const routeMessage = document.getElementById("routeMessage");

routeButton.addEventListener("click", async () => {
    routeContainer.innerHTML = "";
    routeMessage.textContent = "Loading routes...";

    try {
        const response = await fetch("/routes");

        if (!response.ok) {
            throw new Error("Failed to load routes");
        }

        const routes = await response.json();

        routeMessage.textContent = routes.length
            ? ""
            : "No routes available.";

        routes.forEach(route => {
            const card = document.createElement("div");
            card.className = "route-card";

            const heading = document.createElement("h3");
            heading.textContent =
                `${route.source} → ${route.destination}`;

            const distance = document.createElement("p");
            distance.textContent =
                `Distance: ${route.distance_km} km`;

            const duration = document.createElement("p");
            duration.textContent =
                `Duration: ${route.estimated_duration}`;

            card.append(heading, distance, duration);
            routeContainer.appendChild(card);
        });

    } catch (error) {
        routeMessage.textContent = "Unable to load routes.";
        console.error(error);
    }
});


/* SCHEDULES SECTION */

const scheduleButton = document.getElementById("loadSchedules");
const scheduleContainer = document.getElementById("scheduleContainer");
const scheduleMessage = document.getElementById("scheduleMessage");

scheduleButton.addEventListener("click", async () => {
    scheduleContainer.innerHTML = "";
    scheduleMessage.textContent = "Loading schedules...";

    try {
        const response = await fetch("/schedules");

        if (!response.ok) {
            throw new Error("Failed to load schedules");
        }

        const schedules = await response.json();

        scheduleMessage.textContent = schedules.length
            ? ""
            : "No schedules available.";

        schedules.forEach(schedule => {
            const card = document.createElement("div");
            card.className = "schedule-card";

            const heading = document.createElement("h3");
            heading.textContent =
                `${schedule.source} → ${schedule.destination}`;

            const details = [
                `Bus: ${schedule.bus_number}`,
                `Type: ${schedule.bus_type}`,
                `Driver: ${schedule.driver_name}`,
                `Departure: ${schedule.departure_time}`,
                `Arrival: ${schedule.arrival_time}`,
                `Fare: ₹${schedule.fare}`
            ];

            card.appendChild(heading);

            details.forEach(detail => {
                const paragraph = document.createElement("p");
                paragraph.textContent = detail;
                card.appendChild(paragraph);
            });

            scheduleContainer.appendChild(card);
        });

    } catch (error) {
        scheduleMessage.textContent =
            "Unable to load schedules.";
        console.error(error);
    }
});


/* PASSENGER MANAGEMENT */

const passengerButton = document.getElementById("loadPassengers");
const passengerContainer = document.getElementById("passengerContainer");
const passengerMessage = document.getElementById("passengerMessage");

passengerButton.addEventListener("click", async () => {
    passengerContainer.innerHTML = "";
    passengerMessage.textContent = "Loading passengers...";

    try {
        const response = await fetch("/passengers");

        if (!response.ok) {
            throw new Error("Failed to load passengers");
        }

        const passengers = await response.json();

        passengerMessage.textContent = passengers.length
            ? ""
            : "No passengers available.";

        passengers.forEach(passenger => {
            const card = document.createElement("div");
            card.className = "passenger-card";

            const heading = document.createElement("h3");
            heading.textContent = passenger.passenger_name;

            const details = [
                `Passenger ID: ${passenger.passenger_id}`,
                `Email: ${passenger.email}`,
                `Phone: ${passenger.phone}`,
                `Gender: ${passenger.gender}`,
                `Age: ${passenger.age}`
            ];

            card.appendChild(heading);

            details.forEach(detail => {
                const paragraph = document.createElement("p");
                paragraph.textContent = detail;
                card.appendChild(paragraph);
            });

            passengerContainer.appendChild(card);
        });

    } catch (error) {
        passengerMessage.textContent =
            "Unable to load passengers.";
        console.error(error);
    }
});


/* BOOKING MANAGEMENT */

const bookingButton = document.getElementById("loadBookings");
const bookingContainer = document.getElementById("bookingContainer");
const bookingMessage = document.getElementById("bookingMessage");

bookingButton.addEventListener("click", async () => {
    bookingContainer.innerHTML = "";
    bookingMessage.textContent = "Loading bookings...";

    try {
        const response = await fetch("/bookings");

        if (!response.ok) {
            throw new Error("Failed to load bookings");
        }

        const bookings = await response.json();

        bookingMessage.textContent = bookings.length
            ? ""
            : "No bookings available.";

        bookings.forEach(booking => {
            const card = document.createElement("div");
            card.className = "booking-card";

            const heading = document.createElement("h3");
            heading.textContent = booking.passenger_name;

            const details = [
                `Booking ID: ${booking.booking_id}`,
                `Bus Number: ${booking.bus_number}`,
                `Route: ${booking.source} → ${booking.destination}`,
                `Seat Number: ${booking.seat_number}`,
                `Booking Date: ${booking.booking_date}`,
                `Fare: ₹${booking.fare}`,
                `Status: ${booking.booking_status}`
            ];

            card.appendChild(heading);

            details.forEach(detail => {
                const paragraph = document.createElement("p");
                paragraph.textContent = detail;
                card.appendChild(paragraph);
            });

            bookingContainer.appendChild(card);
        });

    } catch (error) {
        bookingMessage.textContent =
            "Unable to load bookings.";
        console.error(error);
    }
});


/* NEW PASSENGER REGISTRATION */

const passengerForm = document.getElementById("passengerForm");
const registrationMessage = document.getElementById("registrationMessage");

passengerForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const passengerData = {
        passenger_name: document.getElementById("passengerName").value.trim(),
        email: document.getElementById("passengerEmail").value.trim(),
        phone: document.getElementById("passengerPhone").value.trim(),
        gender: document.getElementById("passengerGender").value,
        age: Number(document.getElementById("passengerAge").value)
    };

    registrationMessage.textContent = "Registering passenger...";

    try {
        const response = await fetch("/register-passenger", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(passengerData)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Registration failed.");
        }

        registrationMessage.textContent =
            result.message + " Passenger ID: " + result.passenger_id;

        registrationMessage.style.color = "green";

        passengerForm.reset();

    } catch (error) {
        registrationMessage.textContent = error.message;
        registrationMessage.style.color = "red";
        console.error("Registration error:", error);
    }
});




/* TICKET BOOKING SYSTEM */

const ticketBookingForm =
    document.getElementById("ticketBookingForm");

const ticketBookingMessage =
    document.getElementById("ticketBookingMessage");

ticketBookingForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const bookingData = {
        passenger_id: Number(
            document.getElementById("ticketPassengerId").value
        ),
        schedule_id: Number(
            document.getElementById("ticketScheduleId").value
        ),
        seat_number: Number(
            document.getElementById("ticketSeatNumber").value
        )
    };

    ticketBookingMessage.textContent = "Booking ticket...";
    ticketBookingMessage.style.color = "#555";

    const submitButton =
        ticketBookingForm.querySelector('button[type="submit"]');

    submitButton.disabled = true;

    try {
        const response = await fetch("/book-ticket", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(bookingData)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(
                result.error || "Unable to book ticket."
            );
        }

        ticketBookingMessage.textContent =
            result.message + " Booking ID: " + result.booking_id;

        ticketBookingMessage.style.color = "green";

        ticketBookingForm.reset();

    } catch (error) {
        ticketBookingMessage.textContent = error.message;
        ticketBookingMessage.style.color = "red";

        console.error("Ticket booking error:", error);

    } finally {
        submitButton.disabled = false;
    }
});



/* BOOKING CANCELLATION SYSTEM */

const cancelBookingForm =
    document.getElementById("cancelBookingForm");

const cancellationMessage =
    document.getElementById("cancellationMessage");

cancelBookingForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const bookingId = Number(
        document.getElementById("cancelBookingId").value
    );

    if (!Number.isInteger(bookingId) || bookingId < 1) {
        cancellationMessage.textContent =
            "Please enter a valid Booking ID.";
        cancellationMessage.style.color = "red";
        return;
    }

    const confirmed = window.confirm(
        "Are you sure you want to cancel Booking ID " +
        bookingId + "?"
    );

    if (!confirmed) {
        return;
    }

    const submitButton =
        cancelBookingForm.querySelector('button[type="submit"]');

    submitButton.disabled = true;

    cancellationMessage.textContent = "Cancelling ticket...";
    cancellationMessage.style.color = "#555";

    try {
        const response = await fetch("/cancel-ticket", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                booking_id: bookingId
            })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(
                result.error || "Unable to cancel ticket."
            );
        }

        cancellationMessage.textContent =
            result.message + " Booking ID: " + result.booking_id;

        cancellationMessage.style.color = "green";

        cancelBookingForm.reset();

    } catch (error) {
        cancellationMessage.textContent = error.message;
        cancellationMessage.style.color = "red";

        console.error("Cancellation error:", error);

    } finally {
        submitButton.disabled = false;
    }
});
