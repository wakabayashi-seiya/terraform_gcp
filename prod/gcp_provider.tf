provider "google" {
  project = "${var.project_name}"
  region = "${var.region}"
  credentials = "${file("proud-command-267623-c03d54a84755")}"
}

resource "google_compute_instance" "apps_gcp_terraform" {
  name         = "${var.gce_name}"
  machine_type = "${var.machine_type}"
  zone         = "${var.zone}"

  boot_disk {
	  initialize_params {
		size  = 30
		type  = "${var.boot_disk_type}"
		image = "${var.boot_disk_image}"
	  }
	}
	
  network_interface {
    network = "default"
  }

  service_account {
    scopes = ["logging-write", "monitoring-write"]
  }
}