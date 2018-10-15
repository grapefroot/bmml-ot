# Optimal transport maps for distribution preserving operations on latent spaces of Generative Models

## Reproducing experiments
* Prepare GAN models(Faces, MNIST, Rooms) for different generator priors(Normal, Uniform)
* Implement interpolation functions from the paper:
  * 2-point interpolation
  * n-point interpolation
  * vicinity sampling
  * analogies
* Conduct experiments and compare results
## Experiments with VAE
* Prepare VAE models(Faces, MNIST, Rooms) 
* Implement functions from the paper:
  * 2-point interpolation
  * n-point interpolation
  * vicinity sampling
  * analogies
* Implement new interpolation for latent space of VAE
* Conduct experiments and compare results
## Working with missing values
The idea is to check whether it’s possible to combine 2 pictures with missing parts into 1 good image by first mapping into latent space, performing interpolation and then mapping back using decoder(Using different interpolation techniques). So, for this we will need encoder-decoder architecture. We are planning to use VAE for the moment.

## Additional fun stuff(if we have time)
Draw 2 dimensional map of the dataset using vicinity sampling 
