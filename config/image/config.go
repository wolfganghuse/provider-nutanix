package image

import "github.com/crossplane/upjet/pkg/config"

// Configure configures individual resources by adding custom ResourceConfigurators.
func Configure(p *config.Provider) {
	p.AddResourceConfigurator("nutanix_image", func(r *config.Resource) {
		r.ShortGroup = "image"
	})
}
